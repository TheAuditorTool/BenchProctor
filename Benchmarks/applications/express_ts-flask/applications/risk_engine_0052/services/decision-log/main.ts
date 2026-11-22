import express, { Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { recordDecision } from "./decision_record";
import { renderPolicy } from "./render_policy";
import { formatBatch } from "./format_batch";
import { pruneReceipt } from "./prune_receipt";
import { normalizeBatch } from "./normalize_batch";
import { auditWindow } from "./audit_window";
import { resolveWindow } from "./resolve_window";
import { rotateCase } from "./rotate_case";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/recordDecision", recordDecision);
app.post("/renderPolicy/:id", renderPolicy);
app.post("/formatBatch", formatBatch);
app.post("/pruneReceipt", pruneReceipt);
app.post("/normalizeBatch", normalizeBatch);
app.post("/auditWindow", auditWindow);
app.post("/resolveWindow", resolveWindow);
app.post("/rotateCase", rotateCase);

app.listen(3000, "0.0.0.0");
