import express, { Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { storeArchive } from "./archive_store";
import { summarizeConfig } from "./summarize_config";
import { compactIndex } from "./compact_index";
import { archiveSchedule } from "./archive_schedule";
import { formatRedaction } from "./format_redaction";
import { archiveBundle } from "./archive_bundle";
import { verifyPolicy } from "./verify_policy";
import { reconcilePolicy } from "./reconcile_policy";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/storeArchive", storeArchive);
app.post("/summarizeConfig", summarizeConfig);
app.post("/compactIndex", compactIndex);
app.post("/archiveSchedule", archiveSchedule);
app.post("/formatRedaction", formatRedaction);
app.post("/archiveBundle", archiveBundle);
app.post("/verifyPolicy", verifyPolicy);
app.post("/reconcilePolicy/:id", reconcilePolicy);

app.listen(3000, "0.0.0.0");
