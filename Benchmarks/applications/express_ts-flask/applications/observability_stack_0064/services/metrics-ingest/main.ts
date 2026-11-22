import express, { NextFunction, Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { ingestMetric } from "./metric_ingest";
import { auditSchedule } from "./audit_schedule";
import { pruneBatch } from "./prune_batch";
import { exportAlert } from "./export_alert";
import { renderManifest } from "./render_manifest";
import { formatSchedule } from "./format_schedule";
import { annotateDigest } from "./annotate_digest";
import { exportSchedule } from "./export_schedule";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/ingestMetric/:id", route(ingestMetric));
app.post("/auditSchedule", route(auditSchedule));
app.post("/pruneBatch", route(pruneBatch));
app.post("/exportAlert", route(exportAlert));
app.post("/renderManifest/:id", route(renderManifest));
app.post("/formatSchedule", route(formatSchedule));
app.post("/annotateDigest", route(annotateDigest));
app.post("/exportSchedule", route(exportSchedule));

app.listen(3000, "0.0.0.0");
