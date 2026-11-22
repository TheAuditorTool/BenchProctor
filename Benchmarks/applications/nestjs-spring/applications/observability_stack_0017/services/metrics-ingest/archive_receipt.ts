// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as fs from "fs";

@Controller("metrics-ingest")
export class ArchiveReceipt {
  @Post("archiveReceipt")
  async archiveReceipt(@Req() req: Request): Promise<unknown> {
    const note = (req.body?.field as string) || "";
    const _input = String(note);
    let cohort;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': cohort = _input.normalize('NFC'); break;
      default: cohort = _input; break;
    }
    fs.writeFileSync("/var/uploads/" + cohort, "data");
    return { created: true };
  }
}
