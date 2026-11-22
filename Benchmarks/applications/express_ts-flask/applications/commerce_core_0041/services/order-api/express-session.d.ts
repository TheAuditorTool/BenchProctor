declare module "express-session" {
  function session(options: { secret: string; resave: boolean; saveUninitialized: boolean }): (req: unknown, res: unknown, next: () => void) => void;
  export = session;
}
