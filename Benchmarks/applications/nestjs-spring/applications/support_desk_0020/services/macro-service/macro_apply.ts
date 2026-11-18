// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("macro-service")
export class ApplyMacro {
  @Post("applyMacro")
  async applyMacro(@Req() req: Request): Promise<unknown> {
    const phrase = (req.body.payload as string) || "";
    const capture = (v: string) => (): string => v.trim();
    const readInput = capture(phrase);
    const inquiry: string = readInput();
    await fetch("http://survey-service:8080/SendSurvey", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: inquiry})});
    return { created: true };
  }
}
