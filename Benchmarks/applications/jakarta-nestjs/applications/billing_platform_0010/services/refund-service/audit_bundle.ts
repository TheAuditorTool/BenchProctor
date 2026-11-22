// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, Req } from "@nestjs/common";
import { Request } from "express";
import * as jsYaml from "js-yaml";
import { createClient } from "redis";
import * as jsYamlJsTypes from "js-yaml-js-types";

@Controller("refund-service")
export class AuditBundle {
  @Post("auditBundle")
  async auditBundle(@Req() req: Request): Promise<unknown> {
    const _cache = createClient({ url: "redis://cache:6379" });
    await _cache.connect();
    const headline = (await _cache.get("user_data")) || "";
    const _input = String(headline);
    let remittance;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': remittance = _input.normalize('NFC'); break;
      default: remittance = _input; break;
    }
    const reportSpec = jsYaml.load(String(remittance), { schema: jsYaml.DEFAULT_SCHEMA.extend(jsYamlJsTypes.all) }) as { title?: unknown } | null;
    return { title: String(reportSpec?.title ?? "") };
  }
}
