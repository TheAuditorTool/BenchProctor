// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("dispute-service")
export class AnnotateReport {
  @Post("annotateReport")
  async annotateReport(@Req() req: Request): Promise<unknown> {
    const passage = (req.headers["user-agent"] as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const remittance: string = normalize(passage);
    return "<div>" + remittance + "</div>";
  }
}
