import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { appendAudit } from "./audit_append";
import { exportRoster } from "./export_roster";
import { compactHeader } from "./compact_header";
import { annotateSchedule } from "./annotate_schedule";
import { collectDigest } from "./collect_digest";
import { buildConfig } from "./build_config";
import { pruneRecord } from "./prune_record";
import { auditManifest } from "./audit_manifest";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/appendAudit", route(appendAudit));
app.post("/exportRoster", route(exportRoster));
app.post("/compactHeader/:id", route(compactHeader));
app.post("/annotateSchedule", route(annotateSchedule));
app.post("/collectDigest", route(collectDigest));
app.post("/buildConfig", route(buildConfig));
app.post("/pruneRecord", route(pruneRecord));
app.post("/auditManifest", route(auditManifest));

app.listen(3000, "0.0.0.0");
