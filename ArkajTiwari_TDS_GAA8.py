{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMUO9bQ99gWze5vZ3zLl9a2",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/arkajgithub/TDS/blob/main/ArkajTiwari_TDS_GAA8.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "id": "hUBQgxeSkQmW"
      },
      "outputs": [],
      "source": [
        "!pip install streamlit -q\n",
        "import streamlit as st\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "st.title(\"Find the largest among the 3 numbers\")\n",
        "num1 = st.number_input(\"Enter number 1\")\n",
        "num2 = st.number_input(\"Enter number 2\")\n",
        "num3 = st.number_input(\"Enter number 3\")\n",
        "calculate = st.button(\"Find largest number\")\n",
        "\n",
        "def  largest_number(a,b,c):\n",
        "    if a>b and a>c:\n",
        "        return a\n",
        "    elif b>a and b>c:\n",
        "        return b\n",
        "    else:\n",
        "        return c\n",
        "    \n",
        "if calculate:\n",
        "    largest_num=largest_number(num1,num2,num3)\n",
        "    st.write(\"The largest number is:\",largest_num)"
      ],
      "metadata": {
        "id": "iNs3XHNrkbPb"
      },
      "execution_count": 6,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "MnLFzbnMlfmd"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}