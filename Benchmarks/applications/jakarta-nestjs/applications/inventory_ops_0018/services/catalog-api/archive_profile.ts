// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as net from "net";

@Controller("catalog-api")
export class ArchiveProfile {
  @Post("archiveProfile")
  async archiveProfile(@Req() req: Request): Promise<unknown> {
    const transcript = ((await (await fetch("https://api.partner.example/v1/records")).json()) as { data?: string }).data || "";
    const transform = (v: string): string => v.trim();
    const backorder: string = transform(transcript);
    net.connect(80, new URL(String(backorder)).hostname);
    return { created: true };
  }
}
