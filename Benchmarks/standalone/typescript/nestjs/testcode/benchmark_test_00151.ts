// SPDX-License-Identifier: Apache-2.0
import { Body, Controller, Post, UsePipes, ValidationPipe, NotFoundException } from "@nestjs/common";
import { Response } from "express";
import * as shared from "./shared";
const { db } = shared;
import { IsString } from "class-validator";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";

class UserInputDto {
  @IsString()
  payload!: string;
}
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
  @Post("BenchmarkTest00151")
  @UsePipes(new ValidationPipe())
  async BenchmarkTest00151(@Body() dto: UserInputDto): Promise<unknown> {
    const userInput = dto.payload;
    const tokens = String(userInput).split(',').filter((t) => t.length > 0);
    const data = tokens.join(' ');
    const row = (await db.query("SELECT id, name FROM users")).rows.find((r) => r.name === String(data));
    if (!row) { throw new NotFoundException({error:"not found"}); }
    const value = (row as any).name;
    return { created: true };
  }
}
