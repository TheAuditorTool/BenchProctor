import express, { Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { runCycleCount } from "./cycle_count";
import { summarizeHeader } from "./summarize_header";
import { auditStock } from "./audit_stock";
import { annotateSnapshot } from "./annotate_snapshot";
import { annotateSchedule } from "./annotate_schedule";
import { buildSnapshot } from "./build_snapshot";
import { enrichLedger } from "./enrich_ledger";
import { archiveLedger } from "./archive_ledger";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/runCycleCount", runCycleCount);
app.post("/summarizeHeader", summarizeHeader);
app.post("/auditStock", auditStock);
app.post("/annotateSnapshot", annotateSnapshot);
app.post("/annotateSchedule", annotateSchedule);
app.post("/buildSnapshot", buildSnapshot);
app.post("/enrichLedger", enrichLedger);
app.post("/archiveLedger", archiveLedger);

app.listen(3000, "0.0.0.0");
