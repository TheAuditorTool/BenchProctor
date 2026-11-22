import express, { Request, Response } from "express";
import session from "express-session";

import { settleCapture } from "./capture_settle";
import { compactHeader } from "./compact_header";
import { rotateThreshold } from "./rotate_threshold";
import { publishReceipt } from "./publish_receipt";
import { rotateConfig } from "./rotate_config";
import { mergeIndex } from "./merge_index";
import { auditCheckpoint } from "./audit_checkpoint";
import { mergeDigest } from "./merge_digest";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(express.urlencoded({ extended: false }));
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/settleCapture/:id", settleCapture);
app.post("/compactHeader", compactHeader);
app.post("/rotateThreshold", rotateThreshold);
app.post("/publishReceipt", publishReceipt);
app.post("/rotateConfig", rotateConfig);
app.post("/mergeIndex", mergeIndex);
app.post("/auditCheckpoint", auditCheckpoint);
app.post("/mergeDigest", mergeDigest);

app.listen(3000, "0.0.0.0");
