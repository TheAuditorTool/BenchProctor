import express, { NextFunction, Request, Response } from "express";
import session from "express-session";

import { declareCustoms } from "./customs_declare";
import { auditReport } from "./audit_report";
import { reconcileCheckpoint } from "./reconcile_checkpoint";
import { archiveDigest } from "./archive_digest";
import { publishWindow } from "./publish_window";
import { publishSchedule } from "./publish_schedule";
import { publishWaybill } from "./publish_waybill";
import { summarizeLedger } from "./summarize_ledger";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/declareCustoms", route(declareCustoms));
app.post("/auditReport", route(auditReport));
app.post("/reconcileCheckpoint", route(reconcileCheckpoint));
app.post("/archiveDigest", route(archiveDigest));
app.post("/publishWindow", route(publishWindow));
app.post("/publishSchedule", route(publishSchedule));
app.post("/publishWaybill", route(publishWaybill));
app.post("/summarizeLedger", route(summarizeLedger));

app.listen(3000, "0.0.0.0");
