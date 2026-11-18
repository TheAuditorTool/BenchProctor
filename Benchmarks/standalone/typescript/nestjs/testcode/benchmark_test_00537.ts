// SPDX-License-Identifier: Apache-2.0
import { Controller, Post, NotFoundException } from "@nestjs/common";
import { Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

@Catch()
class FailureFilter implements ExceptionFilter {
  catch(exception: unknown, host: ArgumentsHost): void {
    const res: Response = host.switchToHttp().getResponse();
    const status = exception instanceof HttpException ? exception.getStatus() : 500;
    const body = exception instanceof HttpException ? exception.getResponse() : { error: "internal" };
    res.status(status).json(body);
  }
}

@Controller("benchmark")
@UseFilters(FailureFilter)
export class BenchmarkController {
  @Post("BenchmarkTest00537")
  async BenchmarkTest00537(): Promise<unknown> {
    const userInput = process.env.APP_INPUT || "";
    const _input = String(userInput);
    let data;
    switch (_input.startsWith('{') ? 'json' : 'text') {
      case 'json': data = _input.normalize('NFC'); break;
      default: data = _input; break;
    }
    const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
    if (!row) { throw new NotFoundException({error:"not found"}); }
    const value = (row as any).name;
    return { created: true };
  }
}
