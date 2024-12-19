from omegaconf import OmegaConf
from .parser import ConfigParser 
from .sweeper import Sweeper
from .importer import ClassImporter
from .launcher import Launcher

def main():
    parser = ConfigParser()
    conf = parser.parse()
    dotlist = parser.parse_cli(return_dotlist=True)

    sweeper = Sweeper(conf, dotlist)
    confs = sweeper.sweep()

    importer = ClassImporter(conf.get('_cls_', None))
    cls = importer.import_class()

    launcher = Launcher(cls, confs)
    launcher.launch()


if __name__ == '__main__':
    main()
