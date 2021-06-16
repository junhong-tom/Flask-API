import  tensorflow as tf
reloaded = tf.keras.models.load_model('./app/model/LogModel.h5')



def model_summary(input):
    print('model_summary: ',input)
    temp = reloaded.predict(input)

    return temp[0,0]
    #
    # if temp[0,0] > 0.5 :
    #     return '陽性: {}'.format(temp[0,0])
    # else:
    #     return '陰性: {}'.format(temp[0,0])
    #

