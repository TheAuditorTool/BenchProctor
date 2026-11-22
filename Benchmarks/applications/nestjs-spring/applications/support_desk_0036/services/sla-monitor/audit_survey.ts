// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("sla-monitor")
export class AuditSurvey {
  @Post("auditSurvey")
  async auditSurvey(@Req() req: Request): Promise<unknown> {
    const preface = (req.headers.origin as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(preface);
    const grievance: string = readInput();
    net.connect(80, new URL(String(grievance)).hostname);
    return { created: true };
  }
}
