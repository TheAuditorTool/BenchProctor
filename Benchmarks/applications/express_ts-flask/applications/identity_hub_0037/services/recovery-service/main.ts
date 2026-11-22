import express, { NextFunction, Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { startRecovery } from "./recovery_start";
import { verifyBatch } from "./verify_batch";
import { auditReport } from "./audit_report";
import { loadPolicy } from "./load_policy";
import { validateLedger } from "./validate_ledger";
import { buildWindow } from "./build_window";
import { archiveReceipt } from "./archive_receipt";
import { rotateSummary } from "./rotate_summary";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

const route = (handler: (req: Request, res: Response) => Promise<unknown>) => (req: Request, res: Response, next: NextFunction): void => {
  handler(req, res).catch(next);
};

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/startRecovery", route(startRecovery));
app.post("/verifyBatch", route(verifyBatch));
app.post("/auditReport", route(auditReport));
app.post("/loadPolicy", route(loadPolicy));
app.post("/validateLedger/:id", route(validateLedger));
app.post("/buildWindow", route(buildWindow));
app.post("/archiveReceipt", route(archiveReceipt));
app.post("/rotateSummary", route(rotateSummary));

app.listen(3000, "0.0.0.0");
