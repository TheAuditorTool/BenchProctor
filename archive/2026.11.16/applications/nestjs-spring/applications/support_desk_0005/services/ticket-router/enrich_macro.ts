// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("ticket-router")
export class EnrichMacro {
  @Post("enrichMacro")
  async enrichMacro(@Req() req: Request): Promise<unknown> {
    const phrase = (req.headers["user-agent"] as string) || "";
    function normalize(value: string): string { return value.normalize("NFC"); }
    const inquiry: string = normalize(phrase);
    return "<div>" + inquiry + "</div>";
  }
}
