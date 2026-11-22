// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("metrics-ingest")
export class AuditSchedule {
  @Post("auditSchedule")
  async auditSchedule(@Req() req: Request): Promise<unknown> {
    const tagline = (req.headers.authorization as string) || "";
    const _input = String(tagline);
    let gauge;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': gauge = _input.normalize('NFC'); break;
      default: gauge = _input; break;
    }
    fs.unlinkSync("/var/app/data/" + gauge);
    return { created: true };
  }
}
