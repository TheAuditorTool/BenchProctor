// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("preview-renderer")
export class AnnotateSummary {
  @Post("annotateSummary")
  async annotateSummary(@Req() req: Request): Promise<unknown> {
    const footnote = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
    const transform = (v: string): string => v.trim();
    const byline: string = transform(footnote);
    net.connect(80, new URL(String(byline)).hostname);
    return { created: true };
  }
}
