from DE_agent import DE_agent_response
from HoopScout.BA_agent import BA_agent_response
from SR_agent import SR_agent_response
from QE_agent import QE_agent_response

def run():
    quantitative_data = []
    qualitative_data = []
    
    DE_response = DE_agent_response(quantitative_data)
    BA_response = BA_agent_response(qualitative_data)
    
    SR_response = SR_agent_response([DE_response + BA_response])
    
    scouting_report = QE_agent_response(SR_response)
    
    return scouting_report

if __name__ == "__main__":
    report = run()
    print(report)
