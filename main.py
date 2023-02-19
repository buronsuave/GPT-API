from ChatGPTAPI import ChatGPT
from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import JSONFormatter
import os

def create_app():
    app = Flask(__name__)
    return app

def create_session():
    session_token = os.environ.get('GPT_TOKEN', 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..Rgc_diNm1Yx5s7bl.ec5-TU6E-4sa38TWLG8UFukfniKwff0iXTF0TARwzt7glXwAhRpL9gB1WakmbS5RjKODO_tuBc7_vq-U1gUsjmzfsYYCeJ20H359HYwVrMEvkuc3A1Oq5ieWWw79xcKEUCo13EwpNYhXQ856pAG3ws_RkO0pwfVU6r1voB7rAPNo6Q4fiWyLmE91CgURAD41KZPaMJUT1ljXU-lttL4gHFOyjS71YgFPtRZ5oE9T6GYZBQuNt-UmkZfRtMtadrolapuxxFLsHshSZFS8swvM96LOkOUHOz5s4H6Q1tIpppvbsUY4VLrg1yKZb654huAZ0_YPTMTKnR1z3b76oI4kFxUH7YHbqx2mXEA7qrdKU2n9KXB7UGNFcTApM362tRwDZ25uPPSwHuAf0DjlkScVriB8DDbUcQ8qxC20GDYQ74Xz4ihm9hsLPrYxTXGUPiikqk3s0XgKYYRvDRuUhe-lwphsgDu7RTSDvq5emiz_D97vfvFOdpJYw2XdszZTGKgmtD2dT_re6YudwzgsRK9M_2vbMA-PrskD8ggqkz6rlYW5FdXCheJjU2yvN9G8rFU_TnFVSHmHDj1-28GgDtRQxjRENeQhd9ktENU8iwb3Atbw--ML-XsdOSkmr_CNuueBqMPAWg0ciRzafQ6ch9jrLpCtLdEwWz3L2AQrkk2HzrJ3UdrxbRjkCQ8Xd7ch5nsN5TLXlMt1q3EtpOuArEHDs1kQeDOTSie50nnpSh17eVp8jHenMRWRqXDueVJt4sd7dgFxoNut78z-KnHCtIchDzd9fBhSZGbb-kqOqqrmJpIN-1cCR1uvajJJiCStyUNJahJfO7LG5g3RuTwn1ZJW5L8x7oiIiBcIh19ng0p93vTvm8oDmo1DKIX7cybYdvCPUFnt2_4g-oXWFr4_DEHoHXOE57tfEPP4kXjCLEw5Ti05TT8XKrDbyyWYD_sa3nDU1_yslxIe3HrJ1ciBHBDuDqtNEl4dtIwQ9iUaWvH5bvp5l0VPP2U3YaB5_1HvtARf4hqDmmmMxhEH8kBgCQZ7motAwsLHtZiexSJypVPbkz-YR_jG55h9PIEGgrquFViiQDAtua80Ytl2GMZwUMEnPYWvE7VBsqbyL48ZGWbwJuIEvHe62Pp_h_IA4NSusyRfs4xWaoCFkLZPcQeAGpxealQyR6zJPaSYSbXyEKiduLrGNDnEmwhXW0EzzZT0dKqyp4Re_eddvo_Ub15TzRC3xdjTLUrCQF3vLNxxdPhmks04UBG4Q_HcDmt6NEDOe9BB4EvRX0OsyBUzx0o2I2Ek1R5aaP5iH0HT3_j1DeLn6fTS_px409zKmZZnYMeSFPBxx9J598zTuun4ZjARz3VDilEMS8o_qEQDUbMvRcv-zP6hB3KfnhDsBXIcQ8MBMWuRs-zXrOqXZLlmlcdJP79_thgkClMpRtoIAYsf8MNfg1yrupaVuydaPdW2IpuHkb2YGzghJ3FeY-g_OL7XT52lTE95hWwu7HaRbtvf7_2TLea-KQx1dIJP3HSzV5ouCAtcva7fyMlzf24obHIf25ufOguSrZ_lIcJZ4775Rls5nojoI74o9tDuTRLQxfPeJFwYF7sQuIbw8JQV5Q4PpL1ccrquVeML-rWvZUnfzl_TKmrBKcwggi_JYaWxktGo8MFGN4418UMjRFrIisWoXr_xfyj21FOhU20V8vSvPPmbYCDYlXDQcJB8audqqUZoSQ9Wk4UdpT3sMHETKB1YPGid9caECRdkxdhwrOJ6CWBB2GwbjvtToMoZIpeSz44GEgn1Q0Ge5-c92b8OrMVV6rTmNEeZ2OlFNPMWXvAhM0l3T6osJCJ0i0iy8yL3ZFq_S03vRaL41F5R-6dbifFhYMuAiqtjPXZHLCGIE7VN4XLtes36XAik1jLCguoF0GGdM2iQz2LQDK3QEC1Xvne9vwQVfFiLzfg1pNneJDw1o613jpd0gsm_VpUxvtlBqzrFTwf4y7LqTLG206q03WumirWgzjfk-j7NxvhrcxaKIZnQW5EOJPK8PjE6gymR5hxFMUd5UkTbDVNpcsLEcDl4dWiLXXAAJ-O7b18lDQ9RjuZELdnV4JWhdR-SQjdIiisoMNIybdaQZUe0u0dICJpnUVaOM6Pse8rIZAW6_6cZx4GQV9Y_J9Ny2fQV3YrFPUJvcjFYVMgI_ho2ExbWj5GzqCOZWJnU9pwKSBbg_2S4u4L9lz5wtqEoNxsQ7C4GxSgADq4MBA3MHbs-07fGrdPr3yhpnb0zZ5eWf6xcuhUObKfhYBoboXSHCdHe2LQflfRUGxsv5yhEm3Nfqnjsz0lSO3YHGC1_d8f5H8jI1n5pKYUi94Q9wHFcvayfqQBp-52PRIFc7Bc1Safvz1BEIEkl4ILWPRUCzg7yX_fqiVSsLC4f2MF8yBTD6yDiM666Sg1I73vRXuZQQaqkhvoIcFmy7wHho3olPjw20EQPiQv-CS5XXVAO9wsvQFmu5d3lL1fLKVAVxE05qnOJwZZ0rIi-Kk8FWOgk0kt0Ft_LFCOWEv6hFP62IewoxA.0Y5H_P47DvlPRK25Io-0sw')
    api = ChatGPT(session_token, chrome_args=["version_main=108"], verbose=True)  # auth with session token
    return api

# creates flask server

app = create_app()
api = create_session()

@app.route('/test', methods=['POST', 'GET'])
def test():
    return jsonify({'message': 'All good bro, api up and running'}), 200

@app.route('/', methods=['POST', 'GET'])
def create_request():
    json = request.get_json(force=True)
    if json.get('question') is None:
        return jsonify({'message': 'Bad request'}), 400
    question = json.get('question')
    resp = api.send_message(question)
    api.reset_conversation()  # reset the conversation
    api.clear_conversations()  # clear all conversations
    api.refresh_chat_page()  # refresh the chat page
    return jsonify({'message': resp['message']}), 200

@app.route('/transcript', methods=['GET', 'POST'])
def video_transcript():
  json = request.get_json(force=True)
  if json.get('video_ids') is None:
    return jsonify({'message': 'Bad request'}), 400

  video_ids = json.get('video_ids')
  transcript = YouTubeTranscriptApi.get_transcripts(video_ids,
                                                   languages=['es', 'en'])
  trs = []
  for video in transcript:
    for props in video:
      texts = [a_tuple.get('text') for a_tuple in video[props]]
      text = ' '.join(texts)
      trs.append(text)
  
  return jsonify({'transcripts': trs}), 200
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
