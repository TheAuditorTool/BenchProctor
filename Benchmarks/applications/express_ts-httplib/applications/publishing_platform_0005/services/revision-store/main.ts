import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { saveRevision } from "./revision_save";
import { rotateSnapshot } from "./rotate_snapshot";
import { publishManifest } from "./publish_manifest";
import { auditCheckpoint } from "./audit_checkpoint";
import { pruneRoster } from "./prune_roster";
import { rotateSummary } from "./rotate_summary";
import { renderConfig } from "./render_config";
import { mergeSnapshot } from "./merge_snapshot";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/saveRevision", route(saveRevision));
app.post("/rotateSnapshot", route(rotateSnapshot));
app.post("/publishManifest", route(publishManifest));
app.post("/auditCheckpoint", route(auditCheckpoint));
app.post("/pruneRoster", route(pruneRoster));
app.post("/rotateSummary", route(rotateSummary));
app.post("/renderConfig", route(renderConfig));
app.post("/mergeSnapshot", route(mergeSnapshot));

app.listen(3000, "0.0.0.0");
