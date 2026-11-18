import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { cutRelease } from "./release_cut";
import { buildPolicy } from "./build_policy";
import { archiveReport } from "./archive_report";
import { rotateLedger } from "./rotate_ledger";
import { publishCheckpoint } from "./publish_checkpoint";
import { compactReport } from "./compact_report";
import { publishProfile } from "./publish_profile";
import { rotateBundle } from "./rotate_bundle";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/cutRelease", route(cutRelease));
app.post("/buildPolicy", route(buildPolicy));
app.post("/archiveReport", route(archiveReport));
app.post("/rotateLedger", route(rotateLedger));
app.post("/publishCheckpoint", route(publishCheckpoint));
app.post("/compactReport", route(compactReport));
app.post("/publishProfile", route(publishProfile));
app.post("/rotateBundle", route(rotateBundle));

app.listen(3000, "0.0.0.0");
