import express, { Request, Response } from "express";
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
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/declareCustoms", declareCustoms);
app.post("/renderSummary", renderSummary);
app.post("/pruneSchedule", pruneSchedule);
app.post("/auditConfig", auditConfig);
app.post("/annotateHeader", annotateHeader);
app.post("/exportCheckpoint", exportCheckpoint);
app.post("/mergeCheckpoint", mergeCheckpoint);
app.post("/buildWaybill", buildWaybill);

app.listen(3000, "0.0.0.0");
