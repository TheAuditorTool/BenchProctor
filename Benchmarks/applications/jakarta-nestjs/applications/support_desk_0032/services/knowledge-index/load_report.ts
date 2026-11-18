// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("knowledge-index")
export class LoadReport {
  @Post("loadReport")
  async loadReport(@Req() req: Request): Promise<unknown> {
    const note = (req.body as string) || "";
    const inquiry = String(note).split(/[ \t]+/).join(" ");
    http.get(inquiry);
    return { created: true };
  }
}
