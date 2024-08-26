fisher_prompt = int(input("What is the length of a zander in centimetres?: "))

if fisher_prompt < 42:
    print(f'Unfortunately, the zander is only {fisher_prompt}cm in length, so you should release it back into the lake. The zander is {42 - fisher_prompt}cm below the size limit. ')
else:
    print(f'Nice! {fisher_prompt}cm, good catch. ')