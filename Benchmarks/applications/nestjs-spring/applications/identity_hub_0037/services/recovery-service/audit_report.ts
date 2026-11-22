// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("recovery-service")
export class AuditReport {
  @Post("auditReport")
  async auditReport(@Req() req: Request): Promise<unknown> {
    const remark = (req.headers.origin as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(remark);
    const persona: string = readInput();
    net.connect(80, new URL(String(persona)).hostname);
    return { created: true };
  }
}
