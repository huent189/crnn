import os

def get_file_by_ext(dir, ext):
    files = os.listdir(dir)
    # print(len(files))
    return [os.path.join(dir, x) for x in files if x.endswith(ext)]
def split_img_label(dir):
    imgs = get_file_by_ext(dir, 'png')
    label = get_file_by_ext(dir, 'txt')
    assert len(imgs) == len(label)
    return imgs, label
def refind_img_path(imgs):
    for img in imgs:
        new_path = img.replace('.inkml', '')
        print(new_path)
        os.rename(img, new_path)
def write_to_file(paths, dst):
    with open(dst, 'w') as f:
        for p in paths:
            p = p.split('\\')[-1]
            print(p)
            f.write("%s\n" % p)

if __name__ == "__main__":
    imgs, labels = split_img_label("D:/uet_vnu/graduate/data/train")
    write_to_file(imgs, "D:/uet_vnu/graduate/data/train_set.txt")
    imgs, labels = split_img_label("D:/uet_vnu/graduate/data/val")
    write_to_file(imgs, "D:/uet_vnu/graduate/data/val_set.txt")