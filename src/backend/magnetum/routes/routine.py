from flask import request 
from magnetum.services import routine

def init_app(app):

    # CÓDIGO REFERENTE AO ROBÔ
    @app.route('/routine/start') 
    def start_trial():
        routine.execute_trial()  
        return "Success", 200 

    @app.route('/routine/cycle_count')  # Rota para ler número de ciclos (passadas) atual
    def getCycleCount():
        return ({"cycleCount": str(routine.getCurrentCycle())})
    
    # Rota que devolve apenas valor do estado da bomba para o Raspberry
    @app.route('/current_tray')
    def get_current_tray():
        global current_tray
        return {'current_tray': current_tray}
    
    @app.route('/change_tray', methods=['POST'])
    def tray():
        try:
            global current_tray
            json_input = int(request.json['current_tray']) # Pega valor booleano do JSON
            if json_input in [0, 1, 2, 3]:
                current_tray = json_input
                response = {'status': 'success', 'message': 'tray changed'}
            else:
                response = {'status': 'error', 'message': 'invalid value for tray parameter'}
        except Exception as e:
            response = {'status': 'error', 'message': str(e)}
        return response
   