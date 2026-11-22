import express, { Request, Response } from "express";
import session from "express-session";
import multer from "multer";

import { inviteMember } from "./member_invite";
import { annotateSummary } from "./annotate_summary";
import { normalizeRoster } from "./normalize_roster";
import { renderDigest } from "./render_digest";
import { enrichRoster } from "./enrich_roster";
import { verifyHeader } from "./verify_header";
import { renderThreshold } from "./render_threshold";
import { compactSchedule } from "./compact_schedule";

const app = express();
app.use(express.json());
app.use(express.text({ type: ["text/*", "*/xml", "application/xml"] }));
app.use(multer().any());
app.use(session({ secret: process.env.SESSION_SECRET as string, resave: false, saveUninitialized: true }));

app.get("/health", (_req: Request, res: Response) => res.json({ status: "ok" }));
app.post("/inviteMember", inviteMember);
app.post("/annotateSummary/:id", annotateSummary);
app.post("/normalizeRoster", normalizeRoster);
app.post("/renderDigest", renderDigest);
app.post("/enrichRoster", enrichRoster);
app.post("/verifyHeader", verifyHeader);
app.post("/renderThreshold", renderThreshold);
app.post("/compactSchedule", compactSchedule);

app.listen(3000, "0.0.0.0");
