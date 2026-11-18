// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";

@Controller("knowledge-index")
export class SearchKnowledge {
  @Post("searchKnowledge")
  async searchKnowledge(@Req() req: Request): Promise<unknown> {
    const citation = (req.headers["user-agent"] as string) || "";
    const transform = (v: string): string => v.trim();
    const grievance: string = transform(citation);
    await fetch("http://escalation-service:8080/RaiseEscalation", {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({support_payload: grievance})});
    return { created: true };
  }
}
