// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("caption-service")
export class PublishReport {
  @Post("publishReport")
  async publishReport(@Req() req: Request): Promise<unknown> {
    const snippet = (req.headers["user-agent"] as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(snippet);
    const montage: string = readInput();
    return "<div>" + montage + "</div>";
  }
}
