// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("address-validator")
export class SummarizeLabel {
  @Post("summarizeLabel")
  async summarizeLabel(@Req() req: Request): Promise<unknown> {
    const summary = (req.headers["user-agent"] as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(summary);
    const consignment: string = readInput();
    return "<div>" + consignment + "</div>";
  }
}
