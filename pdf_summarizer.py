import pdftotext
import glob
from gensim.summarization.summarizer import summarize


def get_pdf_list(pdf_name):
    f = open(pdf_name, 'rb')
    ret = pdftotext.PDF(f)
    f.close()
    return ret


def list_to_text(pdf_list):
    ret = ''
    for i in pdf_list:
        ret += ' '.join(i.split())
    return ret


if __name__ == '__main__':
    names = glob.glob('pdf/*.pdf')
    for i in names:
        cur_pdf = get_pdf_list(i)
        txt = list_to_text(cur_pdf)
        result = summarize(text=txt, ratio=0.05, split=True)
        f = open('result/' + i.replace('pdf/', '').replace('.pdf', '') + '.txt', 'w')
        for j in result:
            f.write(j)
            f.write('\n')
        f.close()
