// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";

@Controller("activity-feed")
export class AuditMembership {
  @Post("auditMembership")
  async auditMembership(@Req() req: Request): Promise<unknown> {
    const paragraph = (req.headers.origin as string) || "";
    const _raw = paragraph;
    const wording = (_raw && _raw.length > 0) ? _raw : 'default';
    const reportSpec = jsYaml.load(String(wording), { schema: jsYaml.JSON_SCHEMA }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
