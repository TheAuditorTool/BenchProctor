import express, { Request, Response } from "express";
import session from "express-session";

import { recordBounce } from "./bounce_record";
import { verifySchedule } from "./verify_schedule";
import { renderPolicy } from "./render_policy";
import { archiveIndex } from "./archive_index";
import { reconcileBatch } from "./reconcile_batch";
import { enrichHeader } from "./enrich_header";
import { publishCheckpoint } from "./publish_checkpoint";
import { auditLedger } from "./audit_ledger";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/recordBounce", recordBounce);
app.post("/verifySchedule", verifySchedule);
app.post("/renderPolicy", renderPolicy);
app.post("/archiveIndex", archiveIndex);
app.post("/reconcileBatch", reconcileBatch);
app.post("/enrichHeader", enrichHeader);
app.post("/publishCheckpoint", publishCheckpoint);
app.post("/auditLedger", auditLedger);

app.listen(3000, "0.0.0.0");
