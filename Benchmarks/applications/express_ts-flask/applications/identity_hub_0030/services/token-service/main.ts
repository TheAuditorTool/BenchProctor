import express, { Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { mintToken } from "./token_mint";
import { compactIndex } from "./compact_index";
import { summarizeSummary } from "./summarize_summary";
import { formatReport } from "./format_report";
import { buildBatch } from "./build_batch";
import { normalizeHeader } from "./normalize_header";
import { compactConsent } from "./compact_consent";
import { renderReceipt } from "./render_receipt";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/mintToken", mintToken);
app.post("/compactIndex", compactIndex);
app.post("/summarizeSummary", summarizeSummary);
app.post("/formatReport", formatReport);
app.post("/buildBatch", buildBatch);
app.post("/normalizeHeader", normalizeHeader);
app.post("/compactConsent", compactConsent);
app.post("/renderReceipt/:id", renderReceipt);

app.listen(3000, "0.0.0.0");
