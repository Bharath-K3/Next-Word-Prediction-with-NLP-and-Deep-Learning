{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Creating the Prediction Script:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Importing the Libraries\n",
    "\n",
    "from tensorflow.keras.models import load_model\n",
    "import numpy as np\n",
    "import pickle\n",
    "\n",
    "# Load the model and tokenizer\n",
    "\n",
    "model = load_model('nextword1.h5')\n",
    "tokenizer = pickle.load(open('tokenizer1.pkl', 'rb'))\n",
    "\n",
    "def Predict_Next_Words(model, tokenizer, text):\n",
    "    \"\"\"\n",
    "        In this function we are using the tokenizer and models trained\n",
    "        and we are creating the sequence of the text entered and then\n",
    "        using our model to predict and return the the predicted word.\n",
    "    \n",
    "    \"\"\"\n",
    "    for i in range(3):\n",
    "        sequence = tokenizer.texts_to_sequences([text])[0]\n",
    "        sequence = np.array(sequence)\n",
    "        \n",
    "        preds = model.predict_classes(sequence)\n",
    "#         print(preds)\n",
    "        predicted_word = \"\"\n",
    "        \n",
    "        for key, value in tokenizer.word_index.items():\n",
    "            if value == preds:\n",
    "                predicted_word = key\n",
    "                break\n",
    "        \n",
    "        print(predicted_word)\n",
    "        return predicted_word"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your line: at the dull\n",
      "weather\n",
      "Enter your line: collection of textile\n",
      "samples\n",
      "Enter your line: what a strenuous\n",
      "career\n",
      "Enter your line: stop the script\n",
      "Ending The Program.....\n"
     ]
    }
   ],
   "source": [
    "\"\"\"\n",
    "    We are testing our model and we will run the model\n",
    "    until the user decides to stop the script.\n",
    "    While the script is running we try and check if \n",
    "    the prediction can be made on the text. If no\n",
    "    prediction can be made we just continue.\n",
    "\n",
    "\"\"\"\n",
    "\n",
    "# text1 = \"at the dull\"\n",
    "# text2 = \"collection of textile\"\n",
    "# text3 = \"what a strenuous\"\n",
    "# text4 = \"stop the script\"\n",
    "\n",
    "while(True):\n",
    "\n",
    "    text = input(\"Enter your line: \")\n",
    "    \n",
    "    if text == \"stop the script\":\n",
    "        print(\"Ending The Program.....\")\n",
    "        break\n",
    "    \n",
    "    else:\n",
    "        try:\n",
    "            text = text.split(\" \")\n",
    "            text = text[-1]\n",
    "\n",
    "            text = ''.join(text)\n",
    "            Predict_Next_Words(model, tokenizer, text)\n",
    "            \n",
    "        except:\n",
    "            continue"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
