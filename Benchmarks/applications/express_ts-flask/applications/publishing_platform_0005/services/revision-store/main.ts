import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { saveRevision } from "./revision_save";
import { rotateSnapshot } from "./rotate_snapshot";
import { publishManifest } from "./publish_manifest";
import { pruneThreshold } from "./prune_threshold";
import { formatRevision } from "./format_revision";
import { auditManifest } from "./audit_manifest";
import { pruneArticle } from "./prune_article";
import { publishWindow } from "./publish_window";

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
app.post("/pruneThreshold", route(pruneThreshold));
app.post("/formatRevision", route(formatRevision));
app.post("/auditManifest", route(auditManifest));
app.post("/pruneArticle", route(pruneArticle));
app.post("/publishWindow", route(publishWindow));

app.listen(3000, "0.0.0.0");
