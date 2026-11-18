// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("job-service")
export class AuditCheckpoint {
  @Post("auditCheckpoint")
  async auditCheckpoint(@Req() req: Request): Promise<unknown> {
    const notice = (req.query.id as string) || "";
    const persona = Buffer.from(notice, "hex").toString();
    http.get(persona);
    return { created: true };
  }
}
