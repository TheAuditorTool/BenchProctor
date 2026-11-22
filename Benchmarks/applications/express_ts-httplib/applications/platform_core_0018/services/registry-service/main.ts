import express, { Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { registerService } from "./service_register";
import { mergeReport } from "./merge_report";
import { formatReceipt } from "./format_receipt";
import { collectSchedule } from "./collect_schedule";
import { summarizeDigest } from "./summarize_digest";
import { rotateTenant } from "./rotate_tenant";
import { annotateWindow } from "./annotate_window";
import { compactRoster } from "./compact_roster";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/registerService/:id", registerService);
app.post("/mergeReport", mergeReport);
app.post("/formatReceipt", formatReceipt);
app.post("/collectSchedule", collectSchedule);
app.post("/summarizeDigest", summarizeDigest);
app.post("/rotateTenant", rotateTenant);
app.post("/annotateWindow", annotateWindow);
app.post("/compactRoster/:id", compactRoster);

app.listen(3000, "0.0.0.0");
