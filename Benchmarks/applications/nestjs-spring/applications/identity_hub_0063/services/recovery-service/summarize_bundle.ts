// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as http from "http";

@Controller("recovery-service")
export class SummarizeBundle {
  @Post("summarizeBundle")
  async summarizeBundle(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.body as string) || "";
    const persona = String(paragraph).split(/[ \t]+/).join(" ");
    http.get(persona);
    return { created: true };
  }
}
