import express, { NextFunction, Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { declareCustoms } from "./customs_declare";
import { renderSummary } from "./render_summary";
import { pruneSchedule } from "./prune_schedule";
import { auditConfig } from "./audit_config";
import { annotateHeader } from "./annotate_header";
import { exportCheckpoint } from "./export_checkpoint";
import { mergeCheckpoint } from "./merge_checkpoint";
import { buildWaybill } from "./build_waybill";

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
app.post("/declareCustoms", route(declareCustoms));
app.post("/renderSummary", route(renderSummary));
app.post("/pruneSchedule", route(pruneSchedule));
app.post("/auditConfig", route(auditConfig));
app.post("/annotateHeader", route(annotateHeader));
app.post("/exportCheckpoint", route(exportCheckpoint));
app.post("/mergeCheckpoint", route(mergeCheckpoint));
app.post("/buildWaybill/:id", route(buildWaybill));

app.listen(3000, "0.0.0.0");
