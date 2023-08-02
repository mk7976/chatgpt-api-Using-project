from django.shortcuts import render

def chatgpt(request):
    return render(request,'base.html')

def chatgpt1(request):
    import openai

    openai.api_key = "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"
    while (True):
        text = request.POST.get('t1')

        answer = openai.Completion.create(
            engine="text-davinci-003",
            prompt=text,
            temperature=0.6,
            max_tokens=500,
        )
        asd = answer.choices[0].text
        param = {'text1': 'text', 'ans': asd}
        #print(answer.choices[0].text)

        return render(request, 'home.html', param)
