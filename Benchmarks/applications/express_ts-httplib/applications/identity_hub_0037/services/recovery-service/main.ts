import express, { Request, Response } from "express";
import session from "express-session";

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
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/startRecovery", startRecovery);
app.post("/verifyBatch/:id", verifyBatch);
app.post("/auditReport", auditReport);
app.post("/loadPolicy", loadPolicy);
app.post("/validateLedger", validateLedger);
app.post("/buildWindow", buildWindow);
app.post("/archiveReceipt", archiveReceipt);
app.post("/rotateSummary", rotateSummary);

app.listen(3000, "0.0.0.0");
