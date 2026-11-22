declare module "multer" {
  function multer(): { any(): (req: unknown, res: unknown, next: () => void) => void };
  export = multer;
}
