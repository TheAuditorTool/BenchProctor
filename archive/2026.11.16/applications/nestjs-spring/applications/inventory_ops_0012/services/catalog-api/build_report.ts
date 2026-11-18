// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("catalog-api")
export class BuildReport {
  @Post("buildReport")
  async buildReport(@Req() req: Request): Promise<unknown> {
    const phrase = (req.headers["user-agent"] as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const backorder: string = normalize(phrase);
    return "<div>" + backorder + "</div>";
  }
}
