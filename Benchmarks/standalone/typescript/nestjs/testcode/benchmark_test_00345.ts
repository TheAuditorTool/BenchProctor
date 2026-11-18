// SPDX-License-Identifier: Apache-2.0
import { Controller, Headers, Post, BadRequestException } from "@nestjs/common";
import { Response } from "express";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";
import knex from "knex";

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
  @Post("BenchmarkTest00345")
  async BenchmarkTest00345(@Headers("x-custom-header") hdr: string): Promise<unknown> {
    const userInput = hdr || "";
    const tokens = String(userInput).split(',').filter((t) => t.length > 0);
    const data = tokens.join(' ');
    if (!/^[a-zA-Z0-9_.#\-]+$/.test(data)) { throw new BadRequestException({error:"invalid"}); }
    const processed = data;
    const _knex = knex({ client: "sqlite3", connection: { filename: ":memory:" }, useNullAsDefault: true });
    await _knex.raw("SELECT * FROM users WHERE id = '" + processed + "'");
    return { created: true };
  }
}
