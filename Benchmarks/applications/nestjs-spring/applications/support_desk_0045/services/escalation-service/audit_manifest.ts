// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("escalation-service")
export class AuditManifest {
  @Post("auditManifest")
  async auditManifest(@Req() req: Request): Promise<unknown> {
    const remark = (req.body?.payload as string) || "";
    let inquiry;
    try { inquiry = JSON.parse(remark).value || remark; }
    catch (e) { inquiry = remark; }
    net.connect(80, new URL(String(inquiry)).hostname);
    return { created: true };
  }
}
