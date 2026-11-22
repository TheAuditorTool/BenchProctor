// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("sampling-config")
export class SummarizeSchedule {
  @Post("summarizeSchedule")
  async summarizeSchedule(@Req() req: Request): Promise<unknown> {
    const excerpt = (req.headers.host as string) || "";
    const _input = String(excerpt);
    let cohort;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': cohort = _input.normalize('NFC'); break;
      default: cohort = _input; break;
    }
    http.get(cohort);
    return { created: true };
  }
}
