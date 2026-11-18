// SPDX-License-Identifier: Apache-2.0
import { Body, Controller, Post, UsePipes, ValidationPipe } from "@nestjs/common";
import { Response } from "express";
import { IsString } from "class-validator";
import { ArgumentsHost, Catch, ExceptionFilter, HttpException, UseFilters } from "@nestjs/common";
import { Sequelize } from "sequelize";

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
  @Post("BenchmarkTest00108")
  @UsePipes(new ValidationPipe())
  async BenchmarkTest00108(@Body() dto: UserInputDto): Promise<unknown> {
    const userInput = dto.payload;
    let data;
    try { data = JSON.parse(userInput).value || ""; }
    catch (e) { data = String(userInput); }
    const _coerced = parseInt(String(data), 10);
    const parsedId = _coerced;
    const _sequelize = new Sequelize("sqlite::memory:", { logging: false });
    await _sequelize.query("SELECT * FROM users WHERE id = '" + parsedId + "'");
    return { created: true };
  }
}
